pragma solidity ^0.5.0;

contract Random {

    uint256 private _seed = 0;

    /* constructor
     * */
    constructor() public {
    }

    /* create random number
     * */
    function random(uint256 seed) public returns(uint256 ret) {
        require(msg.sender == tx.origin, "MUST_ORIDINARY_ACCOUNT");
        _seed += seed;
        ret = uint256(blockhash(block.number - 1));
        ret = uint256(keccak256(abi.encodePacked(ret, _seed)));
    }

}
