# app_test

[Appium基本应用](Appium基本应用.md)
[客户端专项测试](客户端专项测试.md)

基本的测试和手段:
- 业务测试:
    - 手工测试
    - 接口测试: rest-assured
- 专项测试
    - 端性能测试
        - 耗电量: battery_history、instruments
        - 卡顿测试: block_canary
        - h5 性能测试: devtool、headless、chrome
    - 端场景测试
        - 兼容性测试: mqc、mtc、testin 和 appium、grid、stf
        - 健壮性测试: monkey
        - 弱网测试: facebok、atc 和 proxy定制
        - 安全测试: wvs 和 burpsuite
- 回归测试
    - 接口测试: rest-assured
    - UI 自动化测试: appium
    - 自动遍历回归测试: appcrawler

专项测试（用户维度）:
- 崩溃（crash，弱网）
- 卡顿（掉帧、gc、cpu）
- 响应慢（启动时间、交互响应、H5 加载）
- 发热（cpu，men、io、network、gps等硬件使用）
- 掉电快（硬件占用）
- 兼容行问题（机型覆盖、回归）

专项测试（技术维度）:
- 奔溃: 自动遍历、monkey测试、横竖屏切换、快速进退
- 卡顿（掉帧、gc、cpu）: 卡顿测试、内存泄漏测试、method profile
- 响应慢（启动时间、交互响应、H5加载）: 冷热启动、界面切换、H5性能测试
- 发热（cpu，men、io、network、gps等硬件使用）: method profile、gc统计、io统计、流量统计、硬件使用统计、耗电量分析
- 兼容行问题（机型覆盖、回归）: 兼容性测试、自动化测试、自动遍历、monkey测试



