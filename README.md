# 自动转存
## 简介
本仓库原设计为为云转存公开仓库，已停止维护

## 食用方法
### Fork本仓库
点击页面顶部的Fork按钮，
![Fork](https://github.com/ThankRain/cloud_transfer/raw/master/image/fork.png)

创建一个分支(建议将仓库设置为私有，否则可能有泄露网盘账户的风险)
### 生成 Access Token
点击右上角头像，点击 Settings 进入设置
![头像->Settings](https://github.com/ThankRain/cloud_transfer/raw/master/image/select_settings.png)

下拉列表，点击 Developer settings
![Dev Settings](https://github.com/ThankRain/cloud_transfer/raw/master/image/dev_setting.png)

点击 Personal access token
![Personal access token](https://github.com/ThankRain/cloud_transfer/raw/master/image/personal_access.png)

点击 Generate new token
![Generate new token](https://github.com/ThankRain/cloud_transfer/raw/master/image/generate.png)

Note 为备注，可随意输入
Expiration 为token过期时间，建议设置为 No expiration（安全性较低，适合懒人）
Select Scope 勾选 workflow 即可
![workflow](https://github.com/ThankRain/cloud_transfer/raw/master/image/permission.png)

点击Generate token 生成 token 并复制

### APP 内配置
在 App 中填入您的 Github用户名(如 ThankRain) 、Fork仓库名（cloud_transfer）
![用户名/仓库名](https://github.com/ThankRain/cloud_transfer/raw/master/image/username_repo.png)

以及刚才生成的 token


## 鸣谢(排名不分先后)
### 阿里云盘上传脚本 - Pluto
[https://github.com/Hidove/aliyundrive-uploader](https://github.com/Hidove/aliyundrive-uploader)
### 蓝奏云API - zaxtyson
[https://github.com/zaxtyson/LanZouCloud-API](https://github.com/zaxtyson/LanZouCloud-API)
