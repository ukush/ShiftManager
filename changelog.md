10/10/2025: 
    - Added ShiftPattern model to represent a standard shift pattern
    - Modify shift model to represent an instance of a ShiftPattern


15/10/2025
    - Decided to simplify the models. Removed the 'shift' model and updated the 'Assignment' model to include the shift pattern, date of shift, and the user assigned to the shift. Renamed to 'ShiftAssignment'
        - The reasoning behind this is because the way the 'shift' model was structured, it had a reference to a shift pattern. However, technically all shifts have all patterns, it's just that some of those patterns can be empty - for e.g. if no one is working that pattern. If that's the case, then we can remove the pattern foreign key, in which case all that is left in the shift model is the date and manager.
        - Therefore, it makes more sense to just include the date of the shift and the shift manager to the new ShiftAssignment model, and delete the shift model.
        - Now instead of assigning a pattern to a shift, you assign a user to a shift pattern. If a user is working more than one pattern (a double shift), two assignments can be made. 