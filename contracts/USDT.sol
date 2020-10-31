pragma solidity ^0.5.0;

import "./ERC20.sol";

/**
 * 
 */
contract USDT is ERC20 {
    string public constant name = "USDT";
    string public constant symbol = "USDT";
    uint8 public constant decimals = 18;

    // 1 token = 1 MAGNITUDE wei of Token
    uint256 constant internal MAGNITUDE = 10 ** uint256(decimals);
    uint256 internal constant INITIAL_SUPPLY = 1000000000 * MAGNITUDE;

    /**
     * constructor
     */
    constructor(address owner) public {
        _totalSupply = INITIAL_SUPPLY;
        _balances[owner] = INITIAL_SUPPLY;
        emit Transfer(address(0), owner, INITIAL_SUPPLY);
    }
}
