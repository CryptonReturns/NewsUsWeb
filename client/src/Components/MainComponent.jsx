import React , {Component} from 'react';
import Header from './Header.jsx'
import 'bootstrap/dist/css/bootstrap.css';

export default class MainComponent extends Component {
    constructor(props){
        super(props)
        this.state = {
            isOpen : false
        }
    }

    render(){
        return <Header />
    }
}