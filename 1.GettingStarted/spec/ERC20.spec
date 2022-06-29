/**
        Fill in the TODOs and then investigate the reports.

		To run, execute the following command in terminal/cmd:

		certoraRun contracts/ERC20.sol --verify ERC20:spec/ERC20.spec
**/

rule transferFromDecreasesAllowance {
    env e;
    address from; address to; uint256 amount;

    // TODO

    assert allowanceAfter == allowanceBefore - amount;
}

rule senderCannotIncreaseOwnerAllowance(method f) {
    env e; calldataarg args;
    address sender = e.msg.sender;
    address owner;
    require sender != owner;
    address spender;
    
    // TODO

    assert ownerAllowanceAfter <= ownerAllowanceBefore;
}

rule transferChangesBalances {
    env e;
    address from; address to; uint256 amount;
    require e.msg.sender == from;
    
    // TODO

    assert fromBalanceAfter == fromBalanceBefore - amount && toBalanceAfter == toBalanceBefore + amount;
}
