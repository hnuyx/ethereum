
var MXC = artifacts.require("./MXC.sol");
var log4js = require('log4js');

contract("begining to test MXC", ()=>{

    var logger = log4js.getLogger();
    logger.level = 'info';
    let mxc;

    beforeEach(async() => {
        mxc = await MXC.new();
    });

    it("case 1 random", async() => {
        for(var i = 0; i < 10; i ++){
            var ret = await mxc.random(i);
            var seed = await mxc.getSeed.call();
            logger.info("RANDOM", ret.logs[0].args.random, "SEED:", seed);
        }
    });

})
