pragma solidity >=0.4.21 <0.6.0;

library Search {
    function indexOf(uint[] storage self, uint value)
        public
        view
        returns (uint)
    {
        for (uint i = 0; i < self.length; i++)
            if (self[i] == value) return i;
        return uint(-1);
    }
}

contract Cheese {
    string public chesseid;
    uint public econsump;
    constructor(uint kilowatt) public {
        econsump = kilowatt;
    }
}

contract Vehicle is Cheese {
    address owner;
    address driver;
    address insurer;
    address lender;
    string public brand;
    string public model;
    uint public batterycap;
    uint public batteryhealth;
    uint public batteryvoltage;
    uint public batterycurrent;
    enum State { Created, Locked, Inactive }

    function burnBattery(uint kilowatt) public {
        if (msg.sender == address(owner))
            batterycap -= kilowatt;
    }

    function chargeBattery(uint kilowatt) public {
        if (msg.sender == address(owner))
            batterycap += kilowatt;
    }

    function replaceBattery() public {
        batteryhealth = "renewed";
    }
}