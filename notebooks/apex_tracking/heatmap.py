import torch
import torchvision


class HeatmapModel(torch.nn.Module):
    
    def __init__(self, output_dim, upsample_dims=[128, 128]):
        super(HeatmapModel, self).__init__()
        self.feature_extractor = torchvision.models.resnet18(pretrained=True)
        self.upsample_dims = upsample_dims
        upsample_dims = [512] + upsample_dims
        upsample_layers = []
        for i in range(1, len(upsample_dims)):
            upsample_layers += [
                torch.nn.ConvTranspose2d(upsample_dims[i-1], upsample_dims[i], kernel_size=4, stride=2, padding=1),
                torch.nn.BatchNorm2d(upsample_dims[i]),
                torch.nn.ReLU(),
            ]
#         self.attention = torch.nn.ConvTranspose2d(upsample_dims[0], upsample_dims[-1], kernel_size=4, stride=4, padding=1, output_padding=2)
        self.upsample = torch.nn.Sequential(*upsample_layers)
        self.final = torch.nn.Conv2d(upsample_dims[-1], output_dim, kernel_size=1, stride=1, padding=0)
    
    def forward(self, x):
        x = self.feature_extractor.conv1(x)
        x = self.feature_extractor.bn1(x)
        x = self.feature_extractor.relu(x)
        x = self.feature_extractor.maxpool(x)

        x = self.feature_extractor.layer1(x)
        x = self.feature_extractor.layer2(x)
        x = self.feature_extractor.layer3(x)
        x = self.feature_extractor.layer4(x) # 512x7x7
        
        y = self.upsample(x)
        x = y
#         x = torch.sigmoid(self.attention(x)) * y
        x = self.final(x)
        
        return x

def generate_heatmap(xy, stdev, shape):
    N = len(xy)
    height = shape[0]
    width = shape[1]
    heatmap = torch.zeros((N, height, width))
    y = torch.linspace(-1, 1, height)[:, None]
    x = torch.linspace(-1, 1, width)[None, :]
    for i in range(N):
        heatmap[i] -= (xy[i, 1] - y)**2
        heatmap[i] -= (xy[i, 0] - x)**2
    heatmap = torch.exp(heatmap / stdev**2)
    return heatmap[:, None, :, :]
    