# 自用规则顺序
0. Reject.list and RejectDomain.list（可选）
> 广告过滤
1. Emby.list
> 自用的emby
2. Direct.list
> 包含applecdn和scholar，不包含的版本为Domestic.list
3. Apple.list
> apple服务走的规则 [参考来源](https://royli.dev/blog/2019/better-proxy-rules-for-apple-services)
4. Global.list
> 包含大多数常用的网站和服务
5. LAN

6. GEOIP or ChinaIP or ChinaASN
