# Changelog

## V4.3.3 — 2026-09-03

按用户最终确认的湖南赛区实际执行口径更新：

- 摘要页不显示页码；
- 正文第一页页码从1开始；
- 正文建议29–30页，硬上限30页；
- 附录硬控制20页以内；
- 主论文PDF按摘要1 + 正文30 + 附录20，目标约51页；
- 附录仍要求全部最终完整可运行源程序；
- “非图片PDF”由建议升级为当前 Skill 的硬 Gate；
- LaTeX 成为默认论文生产环境；
- 新增 Hunan Competition Profile；
- 保留 AI工具无需列参考文献、AI声明与详情PDF等上一版判断。

## V4.3.2 — 2026-09-03

依据2026官方文件、组委会常见问题解释和老师注意事项进行规则分层校准：

- 明确30页正文 = 正文主体 + AI工具使用声明 + 参考文献；
- AI工具本身不要求作为参考文献条目；
- AI声明/参考文献无需单独起页；
- 支撑材料清单建议放附录开头；
- 不要求自行进行AIGC率检测；
- 非图片PDF为官方建议，不夸大为淘汰条款；
- 9月7日20:00为全国报名注册节点，校内更早节点仅为内部期限；
- 全国附录不限页，赛区“20页/总51页”只能由正式赛区规则覆盖；
- 摘要必须从页码1开始，纠正“正文第一页从1开始”的错误建议；
- 附录必须包含全部完整、可运行源程序，不能只放核心代码；
- 新增 Regional Override Gate；
- 新增 Structured Deliverable Accuracy Gate；
- 新增 Answer-Accuracy / Reference-Range Audit；
- 强化数学符号的学科惯例与简洁下标规范。

## V4.3.1 — 2026-09-03

依据用户提供的三份 2026 官方文件逐条校准：

- 《全国组委会报名通知2026》
- 《全国大学生数学建模竞赛论文格式规范（2026年修订稿）》
- 《全国大学生数学建模竞赛人工智能工具使用规定（2026年试行）》

新增/修正：
- 区分纸质版与电子版承诺书/编号页；
- 电子论文 ≤20MB、单一 PDF/Word、不压缩；
- 支撑材料 ZIP/RAR ≤20MB；
- 附录必须含文件列表和全部完整可运行代码；
- 补充自主查阅数据/大篇幅中间结果的支撑材料要求；
- 新增 Anonymity & Metadata Gate；
- 新增指导教师/队外人员竞赛期间禁指导/禁讨论 Gate；
- AI 声明按官方模板校准；
- 新增 9月13日20:00 MD5 Integrity Gate；
- 新增 9月13日20:30—9月14日14:00电子上传窗口；
- 明确上传窗口不是额外建模时间。

## V4.3 — 2026-09-03

基于 2026-09-02 CUMCM 赛前培训纪要，并结合 V4.2 已有证据优先架构进行融合更新。

### 融入现有模块的增强
- M0：官方 Rule Profile、动态时间预算、Submission Freeze、Living Paper Evidence Store；
- M1：Scheduled Re-read、Conceptual System Sketch、Mechanism Attribute Classification；
- M2：明确 NP-hard 不等于必须启发式、Controlled Relaxation、Method Maturity Check；
- M3：Timebox & Stop-loss；
- M4：Local Mechanism Replay、R2/R3 Re-read；
- M5：升级为 Living Paper Finalization、信息化章节标题、Case Study 写法、写作顺序与成文顺序分离；
- M6：CUMCM 2026 Rule Profile、Evidence Density、Color+Grayscale Audit、官方 AI 使用规则、竞赛交流合规、Submission Freeze；
- M7：Local Case Study Defense。

### 明确排除
- 自动选题；
- 团队能力评估；
- 三人环境统一；
- NP-hard→必须启发式；
- 必须写满页数；
- 固定16:9论文图；
- 未经官方支持的AI检测传闻。
