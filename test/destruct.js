
var DEST = artifacts.require("./Destruct.sol");
var log4js = require('log4js');

contract("begining to test Destruct", (accs)=>{

    var logger = log4js.getLogger();
    logger.level = 'info';
    let dest;

    beforeEach(async() => {
        dest = await DEST.new();
    });

    it("case 1 destruct", async() => {
        for(var i = 0; i < 10; i ++){
            var ret = await dest.random(i);
            var seed = await dest.getSeed.call();
            logger.info("RANDOM", ret.logs[0].args.random, "SEED:", seed);
        }

        logger.info("destroy");
        await dest.close();

        for(var i = 0; i < 10; i ++){
            var ret = await dest.random(i);
            var seed = await dest.getSeed.call();
            logger.info("RANDOM", ret.logs[0].args.random, "SEED:", seed);
        }
    });

})
