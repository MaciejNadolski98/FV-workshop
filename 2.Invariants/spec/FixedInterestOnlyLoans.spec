
methods {
    periodCount(uint256) returns uint16 envfree
    periodsRepaid(uint256) returns uint256 envfree
    loansLength() returns uint256 envfree
    loanExists(uint256) returns bool envfree
    status(uint256) returns uint8 envfree
}

definition STATUS_CREATED() returns uint8 = 0;
definition STATUS_ACCEPTED() returns uint8 = 1;
definition STATUS_STARTED() returns uint8 = 2;
definition STATUS_REPAID() returns uint8 = 3;
definition STATUS_CANCELED() returns uint8 = 4;
definition STATUS_DEFAULTED() returns uint8 = 5;

definition largeLoansDoNotExist() returns bool = loansLength() < 2^250;

invariant periodsRepaidIsLTEPeriodsCount(uint256 instrumentId)
    periodsRepaid(instrumentId) <= periodCount(instrumentId) 
    {
        preserved {
            require largeLoansDoNotExist();
            requireInvariant periodsRepaidIsLTPeriodsCountWhileLoanIsOutstanding(instrumentId);
            requireInvariant periodsRepaidIsZeroBeforeLoanStart(instrumentId);
        }
    }

invariant periodCountIsPositiveForExistingLoans(uint256 instrumentId)
    (loanExists(instrumentId)) => (periodCount(instrumentId) > 0)

invariant periodsRepaidIsLTPeriodsCountWhileLoanIsOutstanding(uint256 instrumentId)
    (status(instrumentId) == STATUS_STARTED() || status(instrumentId) == STATUS_DEFAULTED()) 
    =>
    (periodsRepaid(instrumentId) < periodCount(instrumentId))
    {
        preserved with (env e) {
            require e.msg.sender != 0;
            require largeLoansDoNotExist();
            requireInvariant periodsRepaidIsZeroBeforeLoanStart(instrumentId);
            requireInvariant periodCountIsPositiveForExistingLoans(instrumentId);
        }
    }

invariant periodsRepaidIsZeroBeforeLoanStart(uint256 instrumentId)
    (!loanExists(instrumentId) || status(instrumentId) == STATUS_CREATED() || status(instrumentId) == STATUS_ACCEPTED() || status(instrumentId) == STATUS_CANCELED())
    =>
    (periodsRepaid(instrumentId) == 0)
    {
        preserved with (env e) {
            require e.msg.sender != 0;
            require largeLoansDoNotExist();
        }
    }

invariant loanLengthIsAboveExistingInstrumentId(uint256 instrumentId)
    (loanExists(instrumentId)) <=> (loansLength() > instrumentId){
        preserved {
            require largeLoansDoNotExist();
        }
    }
