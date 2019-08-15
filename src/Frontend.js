import React from 'react';

const boardWidth=5;
const boardHeight=5;
const boardSize=boardHeight*boardWidth;

class Cell extends React.Component{
    constructor(props){
        super(props);
        this.state={
            value:false
        };
    }
    render() {
        return(
            <button className="cell" onClick={this.props.onClick}>
                {this.props.value}
            </button>
        )
    }
}

class Board extends React.Component{
    renderCell(i){
        return (
            <Cell
                value={this.props.cells[i]}
                onClick={()=>this.props.onClick(i)}
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
                    {this.renderCell(20)}
                    {this.renderCell(21)}
                    {this.renderCell(22)}
                    {this.renderCell(23)}
                    {this.renderCell(24)}
                </div>
            </div>
        )
    }
}

class Game extends React.Component{
    constructor(props) {
        super(props);
        this.state={
            cells: Array(boardSize).fill(0)
        }
    }

    handleClick(i) {
        const currentCells=this.state.cells.slice();
        currentCells[i]=currentCells[i] ? 0:1;
        this.setState({
            cells:currentCells
        })
    }

    render(){
        return(
            <div className={"game"}>
                <div className={"game-board"}>
                    <Board
                        cells={this.state.cells}
                        onClick={i=>this.handleClick(i)}
                    />
                </div>
            </div>
        )
    }
}

export default Game;