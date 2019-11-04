pragma solidity ^0.5.0;

import "./ERC20.sol";

/**
 * 
 */
contract TPToken is ERC20 {
    string public constant name = "TPToken";
    string public constant symbol = "TPT";
    uint8 public constant decimals = 18;

    // 1 token = 1 MAGNITUDE wei of Token
    uint256 constant internal MAGNITUDE = 10 ** uint256(decimals);
    uint256 internal constant INITIAL_SUPPLY = 1000000000 * MAGNITUDE;

    /**
     * constructor
     */
    constructor() public {
        _totalSupply = INITIAL_SUPPLY;
        _balances[msg.sender] = INITIAL_SUPPLY;
    }
}
