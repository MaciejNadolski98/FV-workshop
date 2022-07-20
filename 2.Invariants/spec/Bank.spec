
methods {
    totalFunds() returns uint256 envfree
    aliceFunds() returns uint256 envfree
    bobFunds() returns uint256 envfree
}

invariant solvency1()
    aliceFunds() <= totalFunds() && bobFunds() <= totalFunds()

rule solvency1asARule(method f) {
    require aliceFunds() <= totalFunds() && bobFunds() <= totalFunds();

    env e; calldataarg args;
    f(e, args);

    assert aliceFunds() <= totalFunds() && bobFunds() <= totalFunds();
}

invariant solvency2()
    aliceFunds() + bobFunds() <= totalFunds()
    {
      preserved with (env e) {
        require e.msg.sender != 0xabcdef;
      }
    }

invariant solvency1revised()
    aliceFunds() <= totalFunds() && bobFunds() <= totalFunds()
    {
      preserved with (env e) {
        require e.msg.sender != 0xabcdef;
        requireInvariant solvency2();
      }
    }

rule aliceCanWithdrawFunds() {
    env e; uint256 amount;
    require e.msg.value == 0;

    require e.msg.sender == 0xa11ce;
    require amount <= aliceFunds();

    requireInvariant solvency2();

    withdraw@withrevert(e, amount);

    assert !lastReverted;
}
