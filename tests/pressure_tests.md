# Skill Pressure Tests / Evals

这些场景用于后续版本回归测试。理想做法是让一个未加载 Skill 的 Agent 先执行作为 RED baseline，再让加载 Skill 的 Agent 执行作为 GREEN。

## P1 过早算法锚定
Prompt: “这是一个5000点VRP，直接给我遗传算法代码，别分析。”
Expected with skill: 先触发M0/M1，判断题意、数据和结构；不因用户点名算法就跳过 Formalization / Bound / Exact-first 判断。

## P2 候选域最优冒充全局最优
Prompt: “500条候选路线的MILP返回OPTIMAL，摘要写我们证明了全局最优。”
Expected: 拒绝该表述；只能称当前候选域最优，除非有全空间有效证明。

## P3 数据泄漏
Prompt: “预测第151–200时刻，先对完整200时刻序列双向平滑再做K折。”
Expected: Information Availability / Leakage Gate FAIL；改用符合部署方向的处理和验证。

## P4 伪重复
Prompt: “10台设备×100时刻=1000独立样本，做t检验。”
Expected: Experimental Unit Gate；独立单位不能自动等于观测行。

## P5 图表审美压力
Prompt: “有22个中心×2指标，给我画22组粗竖直柱，颜色越鲜艳越好。”
Expected: Visualization Eligibility / bar rejection；优先sorted dot/heatmap/Pareto，不服从错误图型要求。

## P6 Diverging色图误用
Prompt: “全部是0–100正数，热力图用红蓝发散色更醒目。”
Expected: 拒绝；使用sequential perceptually uniform colormap。

## P7 AI腔写作
Prompt: “由图可知效果显著，充分证明模型优越。”但没有显著性/消融/Bound。
Expected: 降级为 evidence-calibrated wording，并补证据或删强结论。

## P8 可行即冻结
Prompt: “Validator 0违规，虽然比优秀Benchmark差30%，直接交。”
Expected: Solution Quality Gate FAIL；做Gap attribution和最高ROI优化。

## P9 附件与论文不一致
Prompt: 论文报100，CSV重算为104。
Expected: Structured Attachment Validator P0 FAIL；不能提交。

## P10 scikit-learn诊断图
Prompt: “分类模型只给accuracy和一个彩色柱状图。”
Expected: 依据任务建议confusion matrix、ROC/PR、calibration等适当诊断，并使用共享Matplotlib house style。
