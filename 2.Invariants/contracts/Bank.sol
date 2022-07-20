// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract Bank {
  address public constant owner = address(0xabcdef);
  address public constant alice = address(0xa11ce);
  address public constant bob = address(0xb0b);

  uint256 public totalFunds;
  uint256 public aliceFunds;
  uint256 public bobFunds;

  function deposit(uint256 amount) public {
    if (msg.sender == alice) {
      aliceFunds += amount;
      totalFunds += amount;
    }
    if (msg.sender == bob) {
      bobFunds += amount;
      totalFunds += amount;
    }
  }

  function withdraw(uint256 amount) public {
    if (msg.sender == alice) {
      aliceFunds -= amount;
      totalFunds -= amount;
    }
    if (msg.sender == bob) {
      bobFunds -= amount;
      totalFunds -= amount;
    }
  }

  function declareBankrupcy() public {
    require(msg.sender == owner);
    totalFunds = 0;
  }
}
