// Run using:
//      certoraRun FixedInterestOnlyLoans.conf

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

// This is theoretically achievable but practically unfeasible, therefore we can assume it
// without proving it
definition largeLoansDoNotExist() returns bool = loansLength() < 2^250;

// The periodsRepaid is less than or equal periodsCount
invariant periodsRepaidIsLTEPeriodsCount(uint256 instrumentId)
    true // TODO

// The periodCount is *strictly* positive for existing loans
invariant periodCountIsPositiveForExistingLoans(uint256 instrumentId)
    (loanExists(instrumentId)) => (periodCount(instrumentId) > 0)

// The periodsRepaid is less than periodCount while the loan is outstanding
// An outstanding loan has status Started or Defaulted
invariant periodsRepaidIsLTPeriodsCountWhileLoanIsOutstanding(uint256 instrumentId)
    true // TODO

// The periodsRepaid is zero before loan start
// A loan is before start if it doesn't exist or has status Created, Accepted or Canceled
invariant periodsRepaidIsZeroBeforeLoanStart(uint256 instrumentId)
    true // TODO

// instrumentId is an id of an existing loan if and only if it's below loanLength
invariant loanLengthIsAboveExistingInstrumentId(uint256 instrumentId)
    true // TODO
