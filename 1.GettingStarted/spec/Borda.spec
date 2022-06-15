
// Checks that a voter's "registered" mark is changed correctly - 
// if it's false after a function call, it was false before
// if it's true after a function call it either started as true or changed from false to true via registerVoter()
rule registeredCannotChangeOnceSet(method f, address voter){
    env e; calldataarg args;
    bool voterRegBefore; bool voterRegAfter; 
    
    // TODO

    assert (voterRegAfter != voterRegBefore =>
         (!voterRegBefore && voterRegAfter && f.selector == registerVoter(uint8).selector), 
            "voter was registered from an unregistered state, by other function than registerVoter()");
}


/* Explanation on f.selector

 * On the right side of the implication above we see a f.selector.
 * The use of f.selector is very similar to its use in solidity -
 * since f is a parametric method that calls every function in contract in parallel,
 * we specify (or selecting) to address one particular path - when the f.selector was a specific function.
 */


// Checks that a each voted contender's points receieved the correct amount of points
rule correctPointsIncreaseToContenders(address first, address second, address third){
    env e;
    
    // TODO

    assert true; // this can be removed
}

// Checks that a black listed voter cannaot get unlisted
rule onceBlackListedNotOut(method f, address voter){
    env e; calldataarg args;
    bool registeredBefore; bool black_listed_Before; bool black_listed_After;

    // TODO
    
    assert (registeredBefore && black_listed_Before) => black_listed_After, "the specified user got out of the black list";
}

// Checks that a contender's point count is non-decreasing
rule contendersPointsNondecreasing(method f, address contender){
    env e; calldataarg args;
    uint256 pointsBefore; uint256 pointsAfter;
    
    // TODO

    assert (pointsAfter >= pointsBefore);
}
