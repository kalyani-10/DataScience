require('dotenv').config();
const HDWalletProvider = require("@truffle/hdwallet-provider");

const privateKeys = process.env.privatekey_1;

module.exports = {

  networks: {
    
    development: {
     host: "127.0.0.1",     // Localhost (default: none)
     port: 7545,            // Standard Ethereum port (default: none)
     network_id: "*",       // Any network (default: none)
    },
    sepolia: {
      provider: function () {
        return new HDWalletProvider(
          privateKeys.split(','),
          `https://sepolia.infura.io/v3/b182095e60fe47338e785c8c4dd9ae15`// Url to an Ethereum Node
        )
      },
      network_id: 11155111,
      gas: 5500000,
      confirmations: 2,
      timeoutBlocks: 200,
      skipDryRun: true,
      web3Provider: () => new Web3.providers.HttpProvider('https://sepolia.infura.io/v3/b182095e60fe47338e785c8c4dd9ae15')
    }
  },
 
  

  // Set default mocha options here, use special reporters etc.
  mocha: {
    timeout: 100000
  },

  // Configure your compilers
  compilers: {
    solc: {
      version: "0.8.0",    // Fetch exact version from solc-bin (default: truffle's version)
      docker: false,        // Use "0.5.1" you've installed locally with docker (default: false)
      settings: {          // See the solidity docs for advice about optimization and evmVersion
       optimizer: {
         enabled: false,
         runs: 200
       },
       evmVersion: "byzantium"
      }
    },
  },
};
