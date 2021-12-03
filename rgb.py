QImage image(":/image//image/contacts.png");
QRgb rgb = image.pixel(image.width()/2,image.height()/2);
QVector<QRgb> rgbVector = image.colorTable();
for (int i = 0; i < rgbVector.size(); ++i)
{
    if(rgbVector.at(i) == rgb)
    {
        QRgb rgb2 = QColor(0,255,0).rgba();//替换的颜色可以是透明的，比如QColor(0,255,0，0)。
        image.setColor(i,rgb2);
    }
}
————————————————
版权声明：本文为CSDN博主「BIG_C_GOD」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/BIG_C_GOD/article/details/53366022