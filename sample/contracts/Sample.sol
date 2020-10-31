
pragma solidity ^0.5.0;

/* contract Sample for test
 * */
contract Sample {

    uint256 public record;

    event SetRecord(uint256 rec);

    /* constructor
    * */
    constructor() public {
        record = 10;
    }

    /* get seed
     * */
    function setRecord(uint256 rec) public {
        record = rec;
        emit SetRecord(record);
    }
}


