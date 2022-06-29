

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
