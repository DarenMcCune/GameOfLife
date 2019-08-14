import React from 'react';


function Cell(props){
  return (
      <button className="cell" onClick={props.onClick}>
        {props.value}
      </button>
  );
}

class Board extends React.Component{
  renderCell(i){
    return (
        <Cell
          value={this.props.cells[i]}
          onclick={()=>this.props.onClick(i)}
          />
    );
  }

  render(){
    return(
        <div>
          <div className="board-row">
            {this.renderCell(0)}
            {this.renderCell(1)}
            {this.renderCell(2)}
            {this.renderCell(3)}
            {this.renderCell(4)}
          </div>
          <div className="board-row">
            {this.renderCell(5)}
            {this.renderCell(6)}
            {this.renderCell(7)}
            {this.renderCell(8)}
            {this.renderCell(9)}
          </div>
          <div className="board-row">
            {this.renderCell(10)}
            {this.renderCell(11)}
            {this.renderCell(12)}
            {this.renderCell(13)}
            {this.renderCell(14)}
          </div>
          <div className="board-row">
            {this.renderCell(15)}
            {this.renderCell(16)}
            {this.renderCell(17)}
            {this.renderCell(18)}
            {this.renderCell(19)}
          </div>
          <div className="board-row">
            {this.renderCell(0)}
            {this.renderCell(1)}
            {this.renderCell(2)}
            {this.renderCell(1)}
            {this.renderCell(2)}
          </div>
        </div>
    )
  }
}

class Game extends React.Component{
  render(){
    return(
        <div className={"game"}>
          <div className={"game-board"}>
            <Board
              cells={Array(9).fill(null)}
              onClick={i=>this.handleClick}
            />
          </div>
        </div>
    )
  }
  handleClick(i) {
  }
}

export default Game;