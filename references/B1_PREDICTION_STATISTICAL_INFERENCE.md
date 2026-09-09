# B1 预测与统计推断分支

触发：预测、回归、显著性、参数影响、小样本、寿命外推、时序。

执行顺序：

\[
InformationSet
\rightarrow ExperimentalUnit
\rightarrow TargetObservability
\rightarrow SplitDesign
\rightarrow Baseline
\rightarrow CandidateModels
\rightarrow NestedValidation
\rightarrow Uncertainty
\rightarrow Interpretation
\]

强制检查：

1. 预测时真正可用的信息；
2. 是否存在未来泄漏；
3. 独立样本单位是什么；
4. 目标是否右删失/部分观测；
5. 是否有批次/群组；
6. 参数是否非正交；
7. 显著性是否需要置换检验；
8. 多重比较；
9. effect size；
10. OOT/LOO/Group CV 是否比 random split 更合理；
11. 区间覆盖率；
12. 模型结构不确定性。

如果后续要优化：
必须继续进入 B2。
