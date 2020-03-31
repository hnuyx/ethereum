
pragma solidity ^0.5.0;

/* contract MXC for test
 * */
contract MXC {

    uint256 private _seed = 0;

    event Random(uint256 random);

    /* constructor
    * */
    constructor() public {
    }

    /* create random number
    * */
    function random(uint256 seed) public returns(uint256) {
        uint256 ret = 0;
        require(msg.sender == tx.origin, "MUST_ORIDINARY_ACCOUNT");
        _seed += seed;
        ret = uint256(blockhash(block.number - 1));
        ret = uint256(keccak256(abi.encodePacked(ret, _seed)));
        emit Random(ret);

        return ret;
    }

    /* get seed
     * */
    function getSeed() public view returns(uint256) {
        return _seed;
    }
}


