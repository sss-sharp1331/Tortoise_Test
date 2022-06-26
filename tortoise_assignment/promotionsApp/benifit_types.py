from email.policy import default


# Values for benifit_types can be changed here

VOUCHER = "VOUCHER"
CASHBACK = "CASHBACK"
default = CASHBACK
benifit_types = (
    (VOUCHER, "Voucher"),
    (CASHBACK, "Cashback"),
)
