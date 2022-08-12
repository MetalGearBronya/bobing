# bobing
博饼 as a web service


### 需求文档

物理模拟太贵，原理模拟就好

旋转，只可能是上四面

随机时长重ran一个底角

随机时长停止，到达上限停止

### 运行说明

使用

```
python3 server.py 8081
```

在8081端口启动服务器

### 开发说明

双击index.html在浏览器打开工具

### 使用说明

通过nginx配置的路径访问index.html

### 备注

骰子的原始图片来源于微信

使用OpenCV和PS将四点修改为红色

OpenCV修改方法：

使用GIMP或PS的info palette获得要修改的像素位置，对这些像素，使用RGB除255的均值作为黑度，乘255作为红色程度（即将BGR设为[redness, redness, 255]），将R的值从255向下调可以将颜色继续加深（具体原理请查询RGB与HSL，HSV的关系，有许多在线可视化工具）

PS修改方法参考[How To Change BLACK Into ANY COLOR In Photoshop](www.youtube.com/watch?v=pdCKweljMYQ)，混合方式选择颜色或变量，调整输出色阶的白色上界使选区边缘与骰子底色接近即可完成
