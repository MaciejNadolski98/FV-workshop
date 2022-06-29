# Install
```
solc-select
certora-cli
vscode
vscode cvl syntax
```

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
