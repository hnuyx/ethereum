pragma solidity ^0.5.0;

contract Destruct {

    uint256 private _seed = 0;
    address payable public _owner;

    event Random(uint256 random);

    /* constructor
     * */
    constructor() public {
        _owner = msg.sender;
    }

    /* create random number
     * */
    function random(uint256 seed) public returns(uint256 ret) {
        require(msg.sender == tx.origin, "MUST_ORIDINARY_ACCOUNT");
        _seed += seed;
        ret = uint256(blockhash(block.number - 1));
        ret = uint256(keccak256(abi.encodePacked(ret, _seed)));
        emit Random(ret);
    }

    function close() onlyOwner public {
        selfdestruct(_owner);
    }

    modifier onlyOwner() {
        require(msg.sender == _owner, "Ownable: caller is not the owner");
        _;
    }

    /* get seed
     * */
    function getSeed() public view returns(uint256) {
        return _seed;
    }
}
