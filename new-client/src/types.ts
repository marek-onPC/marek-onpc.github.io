import type { IconDefinition } from '@fortawesome/free-brands-svg-icons';

export type AuthCredentials = {
	username: string;
	password: string;
};

export type DynamicContext = {
	[key: string]: any;
};

export type IconSet = {
	icon: IconDefinition;
	color: string;
};

export type NoteType = {
	id: string;
	title: string;
	categories: Array<string>;
	content: string;
};

export type NoteCardType = {
	id: string;
	title: string;
	categories?: Array<string>;
};

export enum HTTPMethods {
	POST = 'POST',
	GET = 'GET',
	DELETE = 'DELETE'
}
