/**
        Fill in the TODOs and then investigate the reports.

		To run, execute the following command in terminal/cmd:

		certoraRun contracts/ERC20.sol --verify ERC20:spec/ERC20.spec
**/

// verify that the transferFrom(...) function always decreases allowance by amount
rule transferFromDecreasesAllowance {
    env e;
    address from; address to; uint256 amount;

    // TODO

    assert allowanceAfter == allowanceBefore - amount;
}

// verify that a user (sender) cannot increase another user's (owner) allowance by calling any public function
rule senderCannotIncreaseOwnerAllowance(method f) {
    env e; calldataarg args;
    address sender = e.msg.sender;
    address owner;
    require sender != owner;
    address spender;
    
    // TODO

    assert ownerAllowanceAfter <= ownerAllowanceBefore;
}

// verify that transfer(...) increases the recipient's balance and decreases the sender's balance
rule transferChangesBalances {
    env e;
    address from; address to; uint256 amount;
    require e.msg.sender == from;
    
    // TODO

    assert fromBalanceAfter == fromBalanceBefore - amount && toBalanceAfter == toBalanceBefore + amount;
}
