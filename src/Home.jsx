import React from 'react';

import { Link } from "react-router-dom";
import Shopping from './Shopping';


const Home = () => {
  return (
    <div>

      <div className='link'> Shopping</div>
      <Link to={Shopping} /> 
      </div>
  )
}
export default Home;