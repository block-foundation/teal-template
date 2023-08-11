<div align="right">

[![GitHub License](https://img.shields.io/github/license/block-foundation/blocktxt?style=flat-square&logo=readthedocs&logoColor=FFFFFF&label=&labelColor=%23041B26&color=%23041B26&link=LICENSE)](https://github.com/block-foundation/teal-template/blob/main/LICENSE)
[![devContainer](https://img.shields.io/badge/Container-Remote?style=flat-square&logo=visualstudiocode&logoColor=%23FFFFFF&label=Remote&labelColor=%23041B26&color=%23041B26)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/block-foundation/teal-template)

</div>

---

<div>
    <img align="right" src="https://raw.githubusercontent.com/block-foundation/brand/master/src/logo/logo_gray.png" width="96" alt="Block Foundation Logo">
    <h1 align="left">PyTeal Template</h1>
    <h3 align="left">Block Foundation Smart Contract Series [Teal]</h3>
</div>

---

<img align="right" width="75%" src="https://raw.githubusercontent.com/block-foundation/brand/master/src/image/repository_cover/block_foundation-structure-03-accent.jpg"  alt="Block Foundation Brand">

### Contents

- [Introduction](#introduction)
- [Colophon](#colophon)

<br clear="both"/>

---

<div align="right">

[![Report a Bug](https://img.shields.io/badge/Report%20a%20Bug-GitHub?style=flat-square&&logoColor=%23FFFFFF&color=%23E1E4E5)](https://github.com/block-foundation/teal-template/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Abug-suspected&projects=&template=bug_report.yml)
[![Request a Feature](https://img.shields.io/badge/Request%20a%20Feature-GitHub?style=flat-square&&logoColor=%23FFFFFF&color=%23E1E4E5)](https://github.com/block-foundation/teal-template/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Abug-suspected&projects=&template=feature_request.yml)
[![Ask a Question](https://img.shields.io/badge/Ask%20a%20Question-GitHub?style=flat-square&&logoColor=%23FFFFFF&color=%23E1E4E5)](https://github.com/block-foundation/teal-template/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Abug-suspected&projects=&template=question.yml)
[![Make a Suggestion](https://img.shields.io/badge/Make%20a%20Suggestion-GitHub?style=flat-square&&logoColor=%23FFFFFF&color=%23E1E4E5)](https://github.com/block-foundation/teal-template/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Abug-suspected&projects=&template=suggestion.yml)
[![Start a Discussion](https://img.shields.io/badge/Start%20a%20Discussion-GitHub?style=flat-square&&logoColor=%23FFFFFF&color=%23E1E4E5)](https://github.com/block-foundation/teal-template/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Abug-suspected&projects=&template=discussion.yml)

</div>

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

---

## Colophon

### Authors

This is an open-source project by the **[Block Foundation](https://www.blockfoundation.io "Block Foundation website")**.

The Block Foundation mission is enabling architects to take back initiative and contribute in solving the mismatch in housing through blockchain technology. Therefore the Block Foundation seeks to unschackle the traditional constraints and construct middle ground between rent and the rigidity of traditional mortgages.

website: [www.blockfoundation.io](https://www.blockfoundation.io "Block Foundation website")

### Development Resources

#### Contributing

We'd love for you to contribute and to make this project even better than it is today!
Please refer to the [contribution guidelines](.github/CONTRIBUTING.md) for information.

### Legal Information

#### Copyright

Copyright &copy; 2023 [Stichting Block Foundation](https://www.blockfoundation.io/ "Block Foundation website"). All Rights Reserved.

#### License

Except as otherwise noted, the content in this repository is licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/), and
code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).

Also see [LICENSE](https://github.com/block-foundation/community/blob/master/src/LICENSE) and [LICENSE-CODE](https://github.com/block-foundation/community/blob/master/src/LICENSE-CODE).

#### Disclaimer

**THIS SOFTWARE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**
