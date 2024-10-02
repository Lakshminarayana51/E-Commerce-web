import React, { useState, useEffect } from 'react';

const Shopping = () => {
  const [apidata, setApidata] = useState(null);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch('https://fakestoreapi.com/products/')
      .then(res => res.json())
      .then(json => setApidata(json))
      .catch(err => setError(err));
  }, []);

  if (error) return <div>Error: {error.message}</div>;
  if (!apidata) return <div>Loading...</div>;

  // Filter the data based on the search input
  const filteredData = apidata.filter(item =>
    item.title.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <div>
        <h1 className="text">Happy Shopping⚜</h1>
      </div>
      <div className='search'>
        <input
          type='text'
          placeholder='Search items'
          className='search-input'
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>
      <div className='titles'>
        {filteredData.map(data => (
          <div key={data.id} className='item'>
            <div className='image-wrap'>
              <img src={data.image} alt={data.title} />
              <div>
                <h3>{data.title}</h3>
                <p className='category'>{data.category}</p>
                <p>Price: ${data.price}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default Shopping;
