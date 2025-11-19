// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

contract SimpleStorage {
    uint256 favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    mapping(string => uint256) public nameToFavoriteNumber;

    People[] public people;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // Consultar informacion no consime gas
    // view  -- mostrar datos
    // pure  -- calculos matematicos

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function pureFuntion(uint256 _number) public pure returns (uint256) {
        return _number * 5;
    }

    // el tipo string debe ser designado como memory o storage
    // memory solo existe en el contexto o funcion
    // storage durara en el tiempo o a largo plazo

    function addPersona(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
