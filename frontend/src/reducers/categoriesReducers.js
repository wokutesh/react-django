const initialState = [];

const CategoriesReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET_CATEGORIES':
      return action.payload;

    default:
      return state;
  }
};

export default CategoriesReducer;
