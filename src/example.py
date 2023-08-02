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
