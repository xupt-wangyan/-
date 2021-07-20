'''
summary可以打印网络结构和参数:
summary(model, input_size=[(3, 256, 256)], batch_size=2, device="cpu")
    model:模型
    input_size:输入shape
    device:训练使用cpu/gpu
'''
import torch
from torchsummary import summary
from nets.yolov4 import YoloBody

if __name__ == "__main__":
    # 需要使用device来指定网络在GPU还是CPU运行
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = YoloBody(9,2).to(device)
    summary(model, input_size=(3, 416, 416))
