// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VulnerableVault {
    address public owner;
    mapping(address => uint256) public balances;

    constructor() {
        owner = msg.sender;
    }

    // Deposit ether into the contract
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    // Vulnerable withdrawal function (Reentrancy + tx.origin)
    function withdraw(uint256 amount) public {
        require(tx.origin == msg.sender, "No contracts allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
}
