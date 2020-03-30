import matplotlib.pyplot as plt
from PIL import Image
plt.rcParams['font.sans-serif']="SimHei"
img=Image.open("d:\\lena.tiff")
img_r,img_g,img_b=img.split()


plt.figure(figsize=(5,5))
plt.subplot(221)
img_r=img.resize((50,50))
img_r=img_r.convert("L")
plt.axis("off")
plt.imshow(img_r,cmap="gray")
plt.title("R-缩放",fontsize=14)


plt.subplot(222)
img_g=img.transpose(Image.FLIP_LEFT_RIGHT)
img_g=img_g.transpose(Image.ROTATE_270)
img_g=img_g.convert("L")
plt.imshow(img_g,cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
plt.axis("off")
img_b=img.crop((0,0,300,300))
img_b=img_b.convert("L")
plt.imshow(img_b,cmap="gray")
plt.title("B-裁剪",fontsize=14)

plt.subplot(224)
plt.axis("off")
plt.imshow(img)
plt.title("RGB",fontsize=14)

img.save("d:\\test.png")
plt.suptitle("图像基本操作",fontsize=20,color='blue')
plt.tight_layout(rect=[0,0,1,0.9])
plt.show()
