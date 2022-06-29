

rule transferFromDecreasesAllowance {
    env e;
    address from; address to; uint256 amount;

    // TODO
    uint256 allowanceBefore = allowance(e, from, e.msg.sender);

    transferFrom(e, from, to, amount);

    uint256 allowanceAfter = allowance(e, from, e.msg.sender);
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
    uint256 ownerAllowanceBefore = allowance(e, owner, spender);

    f(e, args);

    uint256 ownerAllowanceAfter = allowance(e, owner, spender);
    // TODO

    assert ownerAllowanceAfter <= ownerAllowanceBefore;
}

rule transferChangesBalances {
    env e;
    address from; address to; uint256 amount;
    require e.msg.sender == from;
    
    // TODO
    uint256 fromBalanceBefore = balanceOf(e, from);
    uint256 toBalanceBefore = balanceOf(e, to);

    transfer(e, to, amount);

    uint256 fromBalanceAfter = balanceOf(e, from);
    uint256 toBalanceAfter = balanceOf(e, to);
    // TODO

    assert fromBalanceAfter == fromBalanceBefore - amount && toBalanceAfter == toBalanceBefore + amount;
}
