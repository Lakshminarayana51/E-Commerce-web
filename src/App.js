import Shopping from './Shopping';
import './App.css';
import { Routes,Route} from "react-router-dom";
import Home from './Home';


function App() {
  
  return (
    <div className='wrapp'>
     
      {/*<h1 className='wap'> Happy Shopping⚜</h1>*/}
    <Shopping/>
    {/*<Samplecomp data={sampledata}/>*/}


    <Routes>
    <Route path='/' element={<Home/>}/>
 
    {/*<Route path='/Samplecomp' element={<Samplecomp/>}/>*/}
    {/*<Route path='/Shopping' element={<Shopping/>}/>*/}
    </Routes>
    </div>
    
  );
}

export default App; 