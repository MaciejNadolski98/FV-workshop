// Run using:
//      certoraRun FixedInterestOnlyLoans.conf

methods {
    loansLength() returns uint256 envfree
    // TODO
}

definition STATUS_CREATED() returns uint8 = 0;
definition STATUS_ACCEPTED() returns uint8 = 1;
definition STATUS_STARTED() returns uint8 = 2;
definition STATUS_REPAID() returns uint8 = 3;
definition STATUS_CANCELED() returns uint8 = 4;
definition STATUS_DEFAULTED() returns uint8 = 5;

// This is theoretically achievable but practically unfeasible, therefore we can assume it
// without proving it
definition largeLoansDoNotExist() returns bool = loansLength() < 2^250;

// The periodsRepaid is less than or equal periodsCount
invariant periodsRepaidIsLTEPeriodsCount(uint256 instrumentId)
    true // TODO

// The periodCount is *strictly* positive for existing loans
invariant periodCountIsPositiveForExistingLoans(uint256 instrumentId)
    true // TODO

// The periodsRepaid is less than periodCount while the loan is outstanding
invariant periodsRepaidIsLTPeriodsCountWhileLoanIsOutstanding(uint256 instrumentId)
    true // TODO

// The periodsRepaid is zero before loan start
invariant periodsRepaidIsZeroBeforeLoanStart(uint256 instrumentId)
    true // TODO

// instrumentId is an id of an existing loan if and only if it's below loanLength
invariant loanLengthIsAboveExistingInstrumentId(uint256 instrumentId)
    true // TODO
