// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract VotingContract {
    address public owner;
    mapping(address => bool) public hasVoted;
    mapping(string => uint256) public votesCount;

    event Voted(address indexed voter, string candidate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function vote(string memory candidate) public {
        require(!hasVoted[msg.sender], "You have already voted");
        votesCount[candidate]++;
        hasVoted[msg.sender] = true;
        emit Voted(msg.sender, candidate);
    }

    function getVotesCount(string memory candidate) public view returns (uint256) {
        return votesCount[candidate];
    }

    function isOwner() public view returns (bool) {
        return msg.sender == owner;
    }
}
