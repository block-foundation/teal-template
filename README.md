<div align="right">

  [![license](https://img.shields.io/github/license/block-foundation/teal-template?color=green&label=license&style=flat-square)](LICENSE.md)
  ![stars](https://img.shields.io/github/stars/block-foundation/teal-template?color=blue&label=stars&style=flat-square)

</div>

---

<div>
    <img align="right" src="https://raw.githubusercontent.com/block-foundation/brand/master/src/logo/logo_gray.png" width="96" alt="Block Foundation Logo">
    <h1 align="left">PyTeal Template</h1>
    <h3 align="left">Block Foundation</h3>
</div>

---

<p align="center">
    <img src="https://raw.githubusercontent.com/block-foundation/brand/master/src/image/repository_cover/block_foundation-form_follows_finance.jpg"width="100%" height="100%" alt="Block Foundation Containers">
</p>

## Introduction

This is a very simple example of a stateful smart contract on the Algorand blockchain. Stateful smart contracts have access to both global state (shared by all users of the contract) and local state (unique to each user), but this example only uses local state. The "counter" variable is stored in each user's local state, and is incremented by 1 each time that user calls the contract. 

```python
from pyteal import *

def approval_program():
    # This block executes when the smart contract is first initialized.
    # It sets a local variable "counter" to 0 for the sender of the transaction.
    on_initialization = Seq([
        App.localPut(Int(0), Bytes("counter"), Int(0)),
        Return(Int(1))  # This indicates that the initialization was successful.
    ])

    # This block executes on each call to the smart contract after it has been initialized.
    # It increments the "counter" variable by 1 for the sender of the transaction.
    on_call = Seq([
        App.localGetEx(Int(0), App.id(), Bytes("counter")),
        App.localPut(Int(0), Bytes("counter"), Add(Int(1), App.localGet(Int(0), Bytes("counter")))),
        Return(Int(1))  # This indicates that the call was successful.
    ])

    # The Cond function routes execution depending on whether the application is being initialized or called.
    # If the application_id of the transaction is 0, that means the application is being initialized.
    # Otherwise, the application is being called.
    program = Cond(
        [Txn.application_id() == Int(0), on_initialization],
        [Txn.application_id() != Int(0), on_call]
    )

    return program

if __name__ == "__main__":
    # This line compiles the PyTeal code into TEAL (Transaction Execution Approval Language), the bytecode language that Algorand smart contracts are executed in.
    print(compileTeal(approval_program(), mode=Mode.Application))
```

You can find more information on stateful smart contracts and PyTeal in the [Algorand developer documentation](https://developer.algorand.org/docs/features/asc1/stateful/).


## Legal Information

### Copyright

Copyright &copy; 2023 [Block Foundation](https://www.blockfoundation.io/ "Block Foundation website"). All Rights Reserved.

### License

Except as otherwise noted, the content in this repository is licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/), and
code samples are licensed under the [MIT License](https://opensource.org/license/mit/).

Also see [LICENSE](https://github.com/block-foundation/community/blob/master/LICENSE) and [LICENSE-CODE](https://github.com/block-foundation/community/blob/master/LICENSE-CODE).

### Disclaimer

**THIS SOFTWARE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**
