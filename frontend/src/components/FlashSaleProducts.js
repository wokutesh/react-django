import React from "react";

const FlashSaleProducts=({products})=>{
   const flashSaleProducts=products.filter((product)=>product.isFlashSale)
   return(
    <div>
        <h3>Flash Sales</h3>
    </div>
   )
}

export default FlashSaleProducts;
