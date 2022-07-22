# Install
```
pip3 install solc-select
pip3 install certora-cli

solc-select install 0.7.6
solc-select use 0.7.6
```

You will also need a Certora Verification Language syntax highlighter VSC extension and Java JDK version 11 or newer.

More comprehensive installation guide can be found here: https://certora.atlassian.net/wiki/spaces/CPD/pages/7274497/Installation+of+Certora+Prover

# Test

```
cd 1.GettingStarted
certoraRun contracts/Bank.sol --verify Bank:spec/IntegrityOfDeposit.spec
```

At the bottom, you should get a violation like this:
```
ERROR: Prover found violations:
ERROR: [rule] integrityOfDeposit
```
