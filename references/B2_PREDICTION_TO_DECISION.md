# B2 Prediction-to-Decision 分支

当预测模型的输出进入优化模型时执行。

核心链：

\[
Prediction
\rightarrow Calibration
\rightarrow Uncertainty
\rightarrow AdmissionGate
\rightarrow TrustRegion
\rightarrow Optimization
\rightarrow DecisionResolution
\]

## 1. 代理准入
未通过样本外门槛的模型不能支撑连续优化。

## 2. 数据支持域
优化候选必须位于可信插值域。

## 3. 不确定性传播
根据题目选择：
- scenario；
- robust bound；
- chance constraint；
- interval worst-case；
- bootstrap policy evaluation。

## 4. Decision Resolution
新方案预测改善必须大于模型误差/测量分辨率。

## 5. 输出分级
- Formal Recommendation
- Robust Alternative
- Experimental Candidate

不要把三者混为“最优解”。
