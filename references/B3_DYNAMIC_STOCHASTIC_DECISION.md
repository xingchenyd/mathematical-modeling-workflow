# B3 动态与随机决策分支

适用：前期决策后获得新信息，再配置资源。

\[
State_0
\rightarrow FirstStage
\rightarrow Observe\ \xi
\rightarrow UpdateState
\rightarrow Recourse
\rightarrow CompareFrozenPolicy
\]

强制：

1. 冻结信息截面；
2. 一阶段变量不可被未来信息回写；
3. 明确二阶段可调整变量；
4. Monte Carlo 给置信精度；
5. 政策比较优先共同随机数；
6. 跨期资源存在时用 DP/rolling/stochastic program，而非逐期贪心；
7. 报告 Value of Information；
8. 随机场景必须有 seed 和复现文件。
