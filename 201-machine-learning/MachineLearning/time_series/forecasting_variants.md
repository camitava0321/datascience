Time series forecasting neural networks have many variants:
1. Neural network architecture
    - Vanilla LSTM
    - Stacked LSTM
    - Bidirectional LSTM
    - CNN LSTM
    - ConvLSTM

2. The number of independent variables
    - Univariate
    - Multivariate

3. The number of dependent variables (only applies for multivariate)
    - Multiple Input Series (forecast only 1 dependent variables)
    - Multiple Parallel Series (forecast multiple dependent variables)

4. The number of forecast steps
    - Single-step (forecast one step of time ahead)
    - Multi-step (forecast multiple step of time ahead)
        - Vector Output Model (The same as usual archtiecture)
        - Encoder-Decoder Model


There are 5 time series experiments:
- univariate: (1) Vanilla LSTM, (2) univariate (non-stationary), (3) na, (4) step-forward.
- multivariate: (1) All neural network architecture, (2) multivariate (stationary), (3) multiple input series, (4) step-forward.
- parallel: (1) Stacked LSTM, (2) multivariate (stationary), (3) multiple parallel series, (4) step-forward.
- multistep: (1) Stacked LSTM, (2) multivariate (stationary), (3) multiple input series, (4) multi-step.
- encoder_decoder: (1) encoder-decoder with Vanilla LSTM, (2) multivariate (stationary), (3) multiple parallel series, (4) multi-step.
